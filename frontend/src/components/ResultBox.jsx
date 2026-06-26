import "./resultsTable.css";


const cellStyle = {
  padding: "10px 16px",
  textAlign: "left",
};


export const ResultBox = ({results})=>{
    return(
        <div style={{ marginTop: "20px", overflowX: "auto" }}>
      <table
        className="results-table"
        style={{
          borderCollapse: "collapse",
          width: "100%",
        }}
      >
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Party</th>
            <th>State</th>
            <th>Constituency</th>
            <th>Status</th>
            <th>Lok Sabha Terms</th>
            <th>Email</th>
            <th>Phone</th>
          </tr>
        </thead>

        <tbody>
          {results.map((member) => (
            <tr key={member.id}>
              <td>{member.id}</td>
              <td>{member.name}</td>
              <td>{member.party}</td>
              <td>{member.state}</td>
              <td>{member.constituency}</td>
              <td>{member.status}</td>
              <td>{member.loksabha_terms}</td>
              <td>{member.email}</td>
              <td>{member.phone}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
    )
}