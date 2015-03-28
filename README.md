# Hadoop-BDA
Big Data Analytics on Meteorological Data

<h3>Data Generation</h3>
<p>Generating the Meteorological Data for Indian Cities</p>
<p><a href="https://github.com/wolfdale/Hadoop-BDA/blob/master/Data_generator.py">Data Generator</a>
</p>
<p><h3>Usage</h3></p>
<p> Pass The arguments as -month -start_year -end_year  </p>

<h3>Hadoop Important Commands</h3>
<p><ul style="list-style-type:circle">
  <li>Starting the hadoop daemons(all at once) -- hadoop/bin/start-all.sh</li>
  <li>Stoping the hadoop daemons(all at once) -- hadoop/bin/stop-all.sh </li>
  <li>Checking the status of Running Daemons----- jps (Not a feature of hadoop itself)</li>
  <li>Formatting the name node ----------------hadoop/bin/ hadoop namenode -format </li>
  <li>Copying files to hdfs</li>
  <li> delete files from hdfs</li>
  <li>making directory in hdfs</li>
</ul>
</p>
<h3>TroubleShooting</h3>
<a href="https://gist.github.com/wolfdale/b1aeb98c10c3a8b120a0#file-shoot_namenode">Shoot The NameNode</a>
