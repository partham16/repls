# man chmod
# which python
echo -e "\nbefore \`chmod +x main.py\`:"
ls -l main.py
chmod +x main.py
echo -e "\nafter \`chmod +x main.py\`:"
ls -l main.py
echo -e "\nexecution:"
./main.py
