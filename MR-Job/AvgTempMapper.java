import java.io.IOException;
import org.apache.commons.lang.StringUtils;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.MapReduceBase;
import org.apache.hadoop.mapred.Mapper;
import org.apache.hadoop.mapred.OutputCollector;
import org.apache.hadoop.mapred.Reporter;

public class AvgTempMapper extends MapReduceBase
	implements Mapper<LongWritable, Text, Text, IntWritable> {

	public void map(LongWritable key, Text value,
			OutputCollector<Text, IntWritable> output, Reporter reporter)
			throws IOException {
	// Get the line store in array
	String [] line = value.toString().split(",");
	// get the extracted value for mapper i.e. day
	String day = line[0];
	String temp=line[2];
	
	if(StringUtils.isNumeric(temp))
		output.collect(new Text(day), new IntWritable(Integer.parseInt(temp)));
	}

}

