pytest -v
pytest_status=$?
pytest_pass=0
if [ $pytest_status -eq $pytest_pass ]
then
  git add .
  echo "enter a commit message:"
  read commit_comment
  git commit -m "$commit_comment"
  echo "what branch?"
  read branch
  git push origin "$branch"
else
  echo "at least one unit test did not pass"
fi
