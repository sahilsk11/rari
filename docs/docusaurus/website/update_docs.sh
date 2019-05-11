cp -r ./../../img/ static/test
rm -r static/img/
mv static/test/ static/img
npm run build
