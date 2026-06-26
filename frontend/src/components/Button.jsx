export const Button = ({children, onClick})=>{
    return(
        <button
      onClick={onClick}
      style={{
        padding: "10px 20px",
        cursor: "pointer",
      }}
    >
      {children}
    </button>
    )
}