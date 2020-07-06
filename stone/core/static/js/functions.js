function error_toggle(source) {
    checkboxes = document.getElementsByName('error');
    for(var i=0, n=checkboxes.length;i<n;i++) {
      checkboxes[i].checked = source.checked;
    }
  }
