PASSWORD=$(kubectl get secret -n openfaas basic-auth -o jsonpath="{.data.basic-auth-password}" | base64 --decode; echo)
echo -n $PASSWORD | faas-cli login --username admin --password-stdin
cd ~/template/

sudo faas-cli remove -f project3.yml
sudo faas-cli build -f project3.yml --build-arg 'TEST_ENABLED=false'
sudo faas-cli push -f project3.yml
sudo faas-cli deploy -f project3.yml
