export const TextField = ({value, onChange, placeholder})=>{
    return(
        <input
      type="text"
      value={value}
      onChange={(e) => onChange(e.target.value)}
      placeholder={placeholder}
      style={{
        padding: "10px",
        width: "300px",
        marginRight: "10px",
      }}
    />
    )
}