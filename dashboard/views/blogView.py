from django.shortcuts import render, redirect
from dashboard.models import *
from openai import OpenAI
import re
from django.conf import settings


def home(request):
    queryset = Blog.objects.all()

    context = {
        'page': "Home",
        'posts': queryset
    }
    return render(request, 'home.html', context)


def blog_detail(request, id):
    try:
        queryset = Blog.objects.get(id=id)
        context = {'page': "Blog Detail", 'post': queryset}
        return render(request, 'blog_detail.html', context)
    except Blog.DoesNotExist:
        return redirect('home')


from django.http import Http404


def comment(request):
    print('hitting')
    if request.method == 'POST':
        description = request.POST.get('message')
        blog_id = request.POST.get('blog_id')

        blog = Blog.objects.get(id=blog_id)

        Comment.objects.create(
            description=description,
            user=request.user,
            blog=blog
        )
        return redirect('detail', id=blog_id)


def contact_us(request):
    return render(request, 'contact_us.html', context={'page': "Contact Us"})


def create_blog_manually(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        Blog.objects.create(
            title=title,
            description=description,
            image=image,
            user=request.user
        )
        return redirect('create_blog_manually')

    queryset = Blog.objects.all()
    context = {
        'page': 'Create Blog',
        'create_blog': queryset
    }
    return render(request, "create_blog_manually.html", context)


client = OpenAI(api_key=settings.OPENAI_API_KEY)


def create_blog_ai(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        if not description:
            user_prompt = f"""Write an SEO-optimized blog post titled {title}. 
                The post should focus on key points relevant to the topic and adhere to best SEO practices. 
                Include 4-5 well-structured headings to organize the content effectively. 
                Conclude with a comprehensive summary that reinforces the main takeaways.Note Down the Generated Content in HTML"""

            response = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {
                        "role": "user",
                        "content": user_prompt,
                    }
                ],
                model="gpt-4o",
            )
            description = response.choices[0].message.content.strip()
            cleaned_description = re.sub(r'^```\s*html\s*|\s*```$', '', description)

        Blog.objects.create(
            title=title,
            description=cleaned_description,
            image=image,
            user=request.user
        )
        return redirect('create_blog_ai')

    queryset = Blog.objects.all()
    context = {
        'page': 'Create Blog',
        'create_blog_ai': queryset
    }
    return render(request, "create_blog_ai.html", context)


def create_blog(request):
    return render(request, 'create_blog.html', context={'page': "Create Blog"})
