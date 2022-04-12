
import React from 'react';
import { years, months, AccountType, accounts, costCentres } from './utils';
import axios from 'axios';
import { useState, useEffect } from 'react';







function App() {
  const [year, setyear] = useState("Select Year")
  const [month, setmonth] = useState("Select Month")
  const [account, setaccount] = useState("set account")
  const [costcenter, setcostcenter] = useState('select costcenter')
  const [accounttype, setaccounttype] = useState("set accounttype")
  const [prediction, setprediction] = useState('.......')


  useEffect(() => {
    console.log(year)
    console.log(month)
    console.log(account)
    console.log(costcenter)
    console.log(accounttype)
  }, [year, month, account, costcenter, accounttype]);



  // http://localhost:5000

  const submithandler = () => {
    axios.post("https://tfenv.herokuapp.com//predict",
      {
        "Year": year,
        "Month": month,
        "Cost_Centre": costcenter,
        "Account": account,
        "Account_Type": accounttype
      }
    ).then((res) => {
      setprediction(res.data)
      
    })

  };



  return (
    <>
      <div className='bg-blue-900 pt-2'>
      <div className="p-6 bg-blue-500 max-w-sm mx-auto rounded-xl shadow-md flex items-center space-x-4 ">
        <div className="text-xl font-medium text-black px-14">Transactions Forecasting </div>
      </div>
      </div>

      <div className="bg-blue-900 h-full">


        <div className="flex justify-center  py-2">
          <div className="form-floating w-1/3">
            <select className="form-select" value={year} onChange={(e) => { setyear(e.target.value) }} id="floatingSelect" aria-label="Floating label select example">
              <option>Year</option>
              {years.map(
                (yearval) => {
                  return <option key={yearval} value={yearval}>{yearval}</option>
                }
              )}

            </select>
            <label htmlFor="floatingSelect">Select Year</label>
          </div>
        </div>

        <div className="flex justify-center  py-2">
          <div className="form-floating w-1/3">
            <select className="form-select" value={month} onChange={(e) => { setmonth(e.target.value) }} id="floatingSelect" aria-label="Floating label select example">
              <option>Month</option>
              {months.map(
                (monthval) => {
                  return <option key={monthval} value={monthval}>{monthval}</option>
                }
              )}

            </select>
            <label htmlFor="floatingSelect">Select Month</label>
          </div>
        </div>

        <div className="flex justify-center  py-2">
          <div className="form-floating w-1/3">
            <select className="form-select" value={account} onChange={(e) => { setaccount(e.target.value) }} id="floatingSelect" aria-label="Floating label select example">
              <option>Account</option>
              {accounts.map(
                (accountval) => {
                  return <option key={accountval} value={accountval}>{accountval}</option>
                }
              )}

            </select>
            <label htmlFor="floatingSelect">Select Account</label>
          </div>
        </div>

        <div className="flex justify-center  py-2">
          <div className="form-floating w-1/3">
            <select className="form-select" value={costcenter} onChange={(e) => { setcostcenter(e.target.value) }} id="floatingSelect" aria-label="Floating label select example">
              <option>Cost Center</option>
              {costCentres.map(
                (acostCentresval) => {
                  return <option key={acostCentresval} value={acostCentresval}>{acostCentresval}</option>
                }
              )}

            </select>
            <label htmlFor="floatingSelect">Select Cost Center</label>
          </div>
        </div>


        <div className="flex justify-center  py-2">
          <div className="form-floating w-1/3">
            <select className="form-select" defaultValue={accounttype} onChange={(e) => { setaccounttype(e.target.value) }} id="floatingSelect" aria-label="Floating label select example">
              <option>Account Type</option>
              {AccountType.map(
                (AccountTypeval) => {
                  return <option key={AccountTypeval} value={AccountTypeval}>{AccountTypeval}</option>
                }
              )}

            </select>
            <label htmlFor="floatingSelect">Select Account Type</label>
          </div>
        </div>

        <div className='flex justify-center'>
          <input className=" border-2 mb-4 py-2 px-2 border-cyan-600 bg-blue-700 text-gray-50 rounded-lg" type="submit" value="Submit" onClick={submithandler} />
        </div>
        <div className='flex justify-center pb-10 text-slate-100'>
          <h1>The Model Prediction: {prediction }</h1>
        </div>


      </div>

    </>

  );
}

export default App;
