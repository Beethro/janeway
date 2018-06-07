import hashlib
def serve_file(request, file_to_serve, article, public=False):
    :param public: boolean
        return serve_file_to_browser(file_path, file_to_serve, public=public)
def serve_file_to_browser(file_path, file_to_serve, public=False):
    :param public: boolean
    if public:
        response['Content-Disposition'] = 'attachment; filename="{0}"'.format(file_to_serve.public_download_name())
    else:
        response['Content-Disposition'] = 'attachment; filename="{0}{1}"'.format(slugify(filename), extension)


def checksum(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()