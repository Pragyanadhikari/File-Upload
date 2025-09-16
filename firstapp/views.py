from django.shortcuts import render,redirect
from django.contrib import messages
import os
import pandas as pd
from .forms import UploadFileForm
from .models import Product
from django.conf import settings
# Create your views here.

#Allowed extensions and columns and written in tuple as they are immutable
extensions=('.csv','.xlsx','.xls')
columns=('sku','name','category','price','stock_qty','status')

def handle_uploaded_file(f, dest_path):
    """Save uploaded file temporarily."""
    with open(dest_path, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    print(f"✅ File saved temporarily at: {dest_path}")

def save_data(filepath):
    created,updated=0,0
    extension=os.path.splitext(filepath)[1].lower()
    if extension=='.csv':
        df=pd.read_csv(filepath)
    elif extension=='.xlsx' or extension=='.xls':
        df=pd.read_excel(filepath)
    else:
        raise ValueError("Invalid file format")
    
    df.columns=[str(col).strip().lower() for col in df.columns]

    missing_cols=set(columns)-set(df.columns)
    if missing_cols:
        raise ValueError( f"File contains missing columns:{','.join(missing_cols)}")
    
    for _,row in df.iterrows():
        sku=str(row.get('sku')).strip()
        if not sku:
            continue #Since SKU IS unique and every product must have a sku

        name=str(row.get('name',"")).strip()
        category=str(row.get('category',"")).strip()
        try:
            price=float(row.get('price') or 0)
        except Exception:
            price=0.0
        try: 
            stock_quantity=int(row.get('stock_qty') or 0)
        except Exception:
            stock_quantity=0
        status_raw = str(row.get("status", "")).strip().lower()
        status = True if status_raw == "active" else False
        # Insert or update (avoids duplication)
        obj, created_flag = Product.objects.update_or_create(
            sku=sku,
            defaults={
                "name": name,
                "category": category,
                "price": price,
                "stock_qty": stock_quantity,
                "status": status,
            },
        )
        if created_flag:
            created += 1
        else:
            updated += 1
    return {"created": created, "updated": updated}



def upload_file_view(request):
    if request.method=="POST":
        form=UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            upload=request.FILES["file"]
            ext = os.path.splitext(upload.name)[1].lower()
            if ext not in extensions:
                messages.error(request, "Invalid file format. Please upload CSV or Excel.")
                return redirect("upload_file")
            upload_dir=os.path.join(settings.MEDIA_ROOT,'file')
            os.makedirs(upload_dir, exist_ok=True)
            dest_path = os.path.join(upload_dir, upload.name)
            handle_uploaded_file(upload, dest_path)


            try:
                result=save_data(dest_path)
                messages.success(
                    request,
                    f"Import successful: {result['created']} new, {result['updated']} updated.",
                )
            except Exception as e:
                messages.error(request, f"Import failed: {e}")

            finally:
                if os.path.exists(dest_path):
                    os.remove(dest_path) #Since temporary, remove the file using finally block.
            
            return redirect("upload_file")
    
    else:
        form =UploadFileForm()
    return render(request,'firstapp/index.html',{"form":form})

            

