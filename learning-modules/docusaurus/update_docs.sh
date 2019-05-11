cp -r ./../img/ website/static/test
cd website/
rm -r static/img/
mv static/test/ static/img
npm run build
