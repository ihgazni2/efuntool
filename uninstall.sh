pip3 uninstall efuntool
git rm -r dist
git rm -r build
git rm -r efuntool.egg-info
rm -r dist
rm -r build
rm -r efuntool.egg-info
git add .
git commit -m "remove old build"

