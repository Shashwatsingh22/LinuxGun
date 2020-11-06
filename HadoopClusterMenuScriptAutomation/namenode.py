def namenode():
	import os
	print("\t\t\tGive details about namenode:")
	namenode_IP = input("\t\t\tGive IP at which you want to configure namenode:")
	namenode_folder = input("\t\t\tFolder name for namenode:")
	os.system("rm -rf {}".format(namenode_folder))
	os.system("mkdir {}".format(namenode_folder))
	namenode_port = input("\t\t\tGive Port Number at which you want to run namenode service:")
	
	file_hdfs = open("/etc/hadoop/hdfs-site.xml","w")
	hdfs_data =  '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
 
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>dfs.name.dir</name>
<value>{}</value>
</property>
</configuration>\n'''.format(namenode_folder)
	file_hdfs.write(hdfs_data)

	file_core = open("/etc/hadoop/core-site.xml", "w")
	core_data = '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:{}</value>
</property>
</configuration>\n'''.format(namenode_IP,namenode_port)
	file_core.write(core_data)   


	

namenode()
