pytest test_functions.py
git add .
echo "enter a commit message:"
read commit_comment
git commit -m "$commit_comment"
echo "what branch?"
read branch
git push origin "$branch"