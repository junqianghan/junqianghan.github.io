#!/usr/bin/python
#coding=utf-8
import os


def main():
    post_dir = "./_posts"
    local_dir = "./local_posts"
    if not os.path.exists(local_dir):
    	os.mkdir(local_dir)

    posts_web = os.listdir(post_dir)
    posts_local = os.listdir(local_dir)
    posts_remain = [i for i in posts_web if i not in posts_local]

    for post in posts_remain:
    	web_post_name = post_dir+"/"+post
    	local_post_name = local_dir+"/"+post
        print(local_post_name)
    	cp_cmd = "cp {web_post_name} {local_post_name}".format(
    		web_post_name=web_post_name,
    		local_post_name=local_post_name)
    	os.popen(cp_cmd)
    	sed_cmd = "sed -i 's/(\/img\//(\..\/img\//g' {file}".format(
    		file=local_post_name)
    	os.popen(sed_cmd)

if __name__ == "__main__":
    main()
