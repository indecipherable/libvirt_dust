#!/usr/bin/env bash
sudo virt-install --name=$1 --vcpus=2 --memory=3072 --cdrom=$2 --disk $3
