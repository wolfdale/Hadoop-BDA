import java.io.IOException;


import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.FileInputFormat;
import org.apache.hadoop.mapred.FileOutputFormat;
import org.apache.hadoop.mapred.JobClient;
import org.apache.hadoop.mapred.JobConf;


public class AvgTemp {

	public static void main(String[] args) throws IOException {

		 
			
			
			JobConf conf = new JobConf(AvgTemp.class);
			conf.setJobName("AvgMax temperature");
			
			
			FileInputFormat.addInputPath(conf, new Path(args[0]));
			FileOutputFormat.setOutputPath(conf, new Path(args[1]));
			
			conf.setMapperClass(AvgTempMapper.class);
			conf.setReducerClass(AvgTempReducer.class);
			
			conf.setOutputKeyClass(Text.class);
			conf.setOutputValueClass(IntWritable.class);
			
			JobClient.runJob(conf);
			
		}

}
