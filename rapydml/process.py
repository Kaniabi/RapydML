def process_rapydml(filename, output_basename=None, markup='html', no_ack=False):
    import os
    from .compiler import Parser, __file__ as compiler_filename
    from .markuploader import load

    rapydml_dir = os.path.abspath(os.path.dirname(compiler_filename))

    markup_lang = load(markup, rapydml_dir)

    html = Parser(markup_lang)
    if output_basename is None:
        output_basename = '%(basename)s'
    output_basename = output_basename % dict(
        filename=filename,
        basename=os.path.splitext(filename)[0],
        ext=os.path.splitext(filename)[-1]
    )
    output_filename = output_basename + '.' + markup

    with open(output_filename, 'w') as output:
        output.write(html.parse(filename))

    return output_filename
