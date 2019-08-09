set /p commitmsg=input commitmsg:
git add *
git commit -m %a%
git push