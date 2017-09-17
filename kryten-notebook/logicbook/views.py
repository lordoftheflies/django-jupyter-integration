import os

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render


def get_notebook_path(filename):
    return '%s/%s.ipynb' % (settings.JUPYTER_WORKSPACE_ROOT, filename)


# Create your views here.
def notebook_index(request, logicbook_name):
    with open(get_notebook_path(logicbook_name)) as ff:
        from nbconvert.preprocessors import ExecutePreprocessor
        import nbformat
        from nbconvert import HTMLExporter
        from nbconvert.preprocessors.execute import CellExecutionError
        src_notebook = nbformat.reads(ff.read(), as_version=4)  # where ff is file opened with some open("path to logicbook file")

        ep = ExecutePreprocessor(timeout=50, kernel_name='python3')
        ep.preprocess(src_notebook, {})
        html_exporter = HTMLExporter()
        html_exporter.template_file = 'basic'  # basic will skip generating body and html tags.... use "all" to gen all..
        (body, resources) = html_exporter.from_notebook_node(src_notebook)

        print('--------------------------------------------------------------')
        for r in resources:
            print(r)
        print('--------------------------------------------------------------')

        # body have html output
        return HttpResponse(body)


def already_generated_notebook(request, logicbook_name):
    with open(get_notebook_path(logicbook_name)) as ff:
        from nbconvert.preprocessors import ExecutePreprocessor
        import nbformat
        from nbconvert import HTMLExporter
        from nbconvert.preprocessors.execute import CellExecutionError
        src_notebook = nbformat.reads(ff.read(), as_version=4)  # where ff is file opened with some open("path to logicbook file")

        html_exporter = HTMLExporter()
        html_exporter.template_file = 'basic'  # basic will skip generating body and html tags.... use "all" to gen all..
        (body, resources) = html_exporter.from_notebook_node(src_notebook)
        print(body)  # body have html output
