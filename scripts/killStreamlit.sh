#!/bin/sh
kill $(ps aux | grep streamlit | grep -v grep | awk '{print $2}')
