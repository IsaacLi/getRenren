package seven.ili;

import java.io.DataInput;
import java.io.DataOutput;
import java.io.IOException;

import org.apache.hadoop.io.WritableComparable;

public class Edge implements WritableComparable{
	
	private String departureNode;
	private String arrivalNode;
	@Override
	public void readFields(DataInput in) throws IOException {
		departureNode = in.readUTF();
		arrivalNode = in.readUTF();
	}

	@Override
	public void write(DataOutput out) throws IOException {
		out.writeUTF(departureNode);
		out.writeUTF(arrivalNode);
	}

	@Override
	public int compareTo(Object o) {
		Edge edge = (Edge)o;
		int bool = (departureNode.compareTo(edge.departureNode) != 0)
				? departureNode.compareTo(edge.departureNode) : arrivalNode.compareTo(edge.arrivalNode);
		return bool;
	}
	

}
