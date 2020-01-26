from django.db import models
from django.shortcuts import render, redirect

from django.urls import reverse

from management.models import Client, Product




def product_list(request):
    products=Product.objects.all()
    data={
        'products':products
    }
    return render(request, 'product_list.html',data)




def product_detail(request,pk):

    product=Product.objects.get(pk=pk)


    data={
        'Product':product,
    }
    return render(request, 'product_detail.html',data)





def create_product(request,):
    clients=Client.objects.all()
    data={'clients':clients}

    if request.method=='POST':
        name=request.POST.get('name')
        price=request.POST.get('price')
        client_id=request.POST.get('client')
        client=Client.objects.get(id=client_id)
        number=request.POST.get('number')
        image=request.FILES.get('image')
        content=request.POST.get('content')

        try:
            int(price)
            int(number)
        except:
            return render(request, 'create_product.html', data)


        if name:
            product=Product.objects.create(
                name=name,
                price=price,
                client=client,
                number=number,
                image=image,
                content=content,
                )

            return redirect(reverse('product-detail',kwargs={'pk':product.pk}))
    return render(request,'create_product.html',data)



def create_photo(request):
  product=Product.objects.get()
  product.image = request.FILES['image']





def create_client(request):
    if request.method=='POST':
        name=request.POST.get('name',None)
        phone =request.POST.get('phone',None)
        adress=request.POST.get('adress',None)


        if name and phone and adress:
            client=Client.objects.create(
                name=name,
                phone=phone,
                adress=adress
            )
            return redirect(reverse('client-detail',kwargs={'pk':client.pk}))
    return render(request,'create_client.html')

def modify_client(request, pk):
    client = Client.objects.get(pk=pk)
    data={
        'client':client
          }

    if request.method=='POST':
        name = request.POST.get('name', None)
        phone = request.POST.get('phone', None)
        adress = request.POST.get('adress', None)
        if name and phone and adress:
            client.name=name
            client.phone=phone
            client.adress=adress
            client.save()
            return redirect(reverse('client-detail', kwargs={'pk': client.pk}))
    return render(request, 'modify_client.html', data)


def modify_product(request,pk):

    clients=Client.objects.all()
    product = Product.objects.get(pk=pk)
    data={'clients':clients, 'product':product}

    if request.method=='POST':

        try:
            int(request.POST.get('price'))
            int(request.POST.get('number'))
        except:
            return render(request,'modify_product.html',data)


        if request.POST.get('name'):
            product.name=request.POST.get('name')
            product.price=request.POST.get('price')
            client_id = request.POST.get('client')
            product.client=Client.objects.get(id=client_id)
            product.number=request.POST.get('number')
            product.content = request.POST.get('content')

            if request.FILES.get('image'):
                product.image=request.FILES.get('image')

            product.save()


            return redirect(reverse('product-detail',kwargs={'pk':product.pk}))
    return render(request,'modify_product.html',data)


def delete_client(request, pk):
    client=Client.objects.get(pk=pk)
    client.delete()
    return redirect(reverse('client-list'))


def delete_product(request,pk):
    product=Product.objects.get(pk=pk)
    product.delete()
    return redirect(reverse('product-list'))

def client_list(request):
    clients=Client.objects.all()
    products=Product.objects.all()
    data={
        'clients':clients,
        'products':products,
    }
    return render(request,'client_list.html',data)




def client_detail(request,pk):
    client=Client.objects.get(pk=pk)
    products=Product.objects.all()
    data={
        'Client':client, 'products':products
    }
    return render(request, 'client_detail.html',data)





def plus(request,pk):
    product=Product.objects.get(pk=pk)
    product.number+=1
    product.save()
    return redirect(reverse('product-list'))


def minus(reqest,pk):
    product = Product.objects.get(pk=pk)
    product.number -= 1
    product.save()
    return redirect(reverse('product-list'))