import java.io.IOException;



import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.MapReduceBase;
import org.apache.hadoop.mapred.OutputCollector;
import org.apache.hadoop.mapred.Reducer;
import org.apache.hadoop.mapred.Reporter;
import java.util.Iterator;




public class AvgTempReducer extends MapReduceBase
	implements Reducer<Text, IntWritable, Text, IntWritable> {

	public void reduce(Text key,Iterator<IntWritable> values,
			OutputCollector<Text, IntWritable> output,Reporter reporter)
			throws IOException {
		
		int sumTemp = 0;
		int numItems=0;
		
		while (values.hasNext()){
			sumTemp+=values.next().get();
			numItems+=1;
			
		}
		
		output.collect(key, new IntWritable(sumTemp/numItems));

}

	
	
}
