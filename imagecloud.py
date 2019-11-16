from cloudinary.compat import StringIO
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url

# {% load cloudinary %}

def upload_image(file_to_upload, name):
    str_file = StringIO(file_to_upload)
    str_file.name = name
    upload_result = upload(str_file)
    image_url = upload_result['url']
    return image_url


