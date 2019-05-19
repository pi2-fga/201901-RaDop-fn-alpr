#!/bin/bash
#
# Purpose: Continuous deploy on production environment
#
# Author: João Pedro Sconetto <sconetto.joao@gmail.com>

curl -sSL https://cli.openfaas.com | sudo sh

echo $DOCKERHUB_PASS | docker login --username $DOCKERHUB_USER --password-stdin 

faas-cli -f fn-alpr.yml build

faas-cli -f fn-alpr.yml push