import React, { useState, useEffect } from 'react'
import axios from 'axios'
import '../App.css';


export default function Imageupload() {

    const [file, setfile] = useState(null)
    const [disease, setdisease] = useState('processing')
    const [confidence, setconfidence] = useState('processing')

    const filehandler = (event) => {
        setfile(event.target.files[0]);
    };

    const clickhandler = () => {
        let fd = new FormData
        fd.append('file', file);

        axios.post("https://potato-desiese-classification.herokuapp.com/predict", fd)
            .then((res) => {
                setdisease(res.data.class)
                setconfidence(res.data.confidence)
            });


    };

    return (
    
            <div className='pt-5'>
                <div className="container">
                    <input type="file" onChange={filehandler} />
                    <br />
                    <button className='btn btn-primary mt-3' onClick={clickhandler}>Submit</button>
                </div>
                <div className="container">
                    <h2>Result-</h2>
                    <p>Class: {disease}</p>
                    <p>Confidence: {confidence}</p>
                </div>
            </div>

    )
}
