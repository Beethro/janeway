
def serve_file(request, file_to_serve, article):
        return serve_file_to_browser(file_path, file_to_serve)
def serve_file_to_browser(file_path, file_to_serve):
    response['Content-Disposition'] = 'attachment; filename="{0}{1}"'.format(slugify(filename), extension)