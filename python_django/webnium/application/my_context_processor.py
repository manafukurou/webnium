def common(request):
  javascript_list = {
    "parts/parts.js",
    "application/Sortable.js",
    "application/jquery-3.5.1.min.js"
  }
  css_list = {
    "application/bootstrap.min.css"
  }
  context = {
      'title': "webnium",
      'javascript_list':  javascript_list,
      'css_list':  css_list,
  }
  return context
