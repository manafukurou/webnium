def common(request):
  javascript_commonlist = {
    "application/Sortable.js",
    "application/jquery-3.5.1.min.js"
  }
  css_commonlist = {
    "application/bootstrap.min.css"
  }
  context = {
      'title': "webnium",
      'css_commonlist':  css_commonlist,
      'javascript_commonlist':  javascript_commonlist,
  }
  return context
