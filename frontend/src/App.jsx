import { useState } from "react";
import { TextField } from "./components/TextField";
import { ResultBox } from "./components/ResultBox";
import { Button } from "./components/Button";
import axios from 'axios'
import api from "./baseUrl";

function App() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSearch = async () => {
    if (!query.trim()) {
      return;
    }

    try {
      setLoading(true);

      const { data } = await api.get(
        "http://localhost:8080/api/search",
        {
          params: {
            q: query,
          },
        }
      );

      setResponse(data);
    } catch (error) {
      console.error(error);
      alert("Failed to fetch results.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        marginTop: "100px",
      }}
    >
      <h2>Search Members</h2>

      <div>
        <TextField
          value={query}
          onChange={setQuery}
          placeholder="Enter data..."
        />
        <Button onClick={handleSearch}>{loading ? "Searching..." : "Search"}</Button>
      </div>

      {response && (
        <>
          <p>
            Found {response.results.length} result(s) for "{response.query}"
          </p>

          <ResultBox results={response.results} />
        </>
      )}
    </div>
  );
}

export default App;