package seven.ili;

import java.io.DataOutput;
import java.io.IOException;
import java.net.URL;

import org.apache.hadoop.io.Writable;

public class URLWritable implements Writable{
	protected URL url;
	public URLWritable() {};
	public URLWritable(URL url){
		this.url = url;
	}
	
	public void write(DataOutput out) throws IOException{
		out.writeUTF(url.toString());
	}

}
