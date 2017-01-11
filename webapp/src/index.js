import './css/font-awesome.min.css'
import 'bootstrap/dist/css/bootstrap.css'
import './index.css';

const CashflowView = require("./views/cashflow")

let cashflowView = new CashflowView({hello: "hai"})
cashflowView.init()

console.log("initialized")