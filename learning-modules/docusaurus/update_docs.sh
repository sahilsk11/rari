cp -r ./../img/ website/static/test
cd website/
rm -r static/img/
mv static/test/ static/img
npm run build
cp static/css/organize.css build/doc-website/css/organize.css
