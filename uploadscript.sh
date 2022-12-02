#!/bin/sh
#echo `date` $UPLOAD_USER has upload file $1 with size $UPLOAD_SIZE >> /var/log/uploadscript.log
#echo $1 >> /var/log/uploadscript.log

#[ ${UPLOAD_USER} == "ftp" ] && UPLOAD_USER="anonymous"

if [ ${1##*.} = "exe" ]; then
	ftp_log="${1} violate file detected. Uploaded by ${UPLOAD_USER}"
	echo "${ftp_log}" >> /home/ftp/public/pureftpd.viofile
	mv ${1} /home/ftp/hidden/.exe/
fi

#user_dir="/home/${UPLOAD_USER}"
#upload_dir="/vol/web_hosting/${user_dir}/public_html"
#! [ -f "${UPLOAD_DIR}" ] && mkdir -p "${upload_dir}"
#echo "${ftp_log}" >> "${upload_dir}/uploadscript.log"
