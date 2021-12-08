#conda activate grade_eval
cd script
echo "TEST "${1}
bash inference.sh eval_${1}