import './index.css';

const CashflowView = require("./views/cashflow")

let cashflowView = new CashflowView({hello: "hai"})
cashflowView.init()

console.log("initialized")