import { useState, useEffect } from 'react';

interface Props {
    businessDetails: BusinessDetails;
    onBack: () => void;
}

const ReviewAndSubmit = ({ businessDetails, onBack }: Props) => {
    const [balanceSheet, setBalanceSheet] = useState<BalanceSheetItem[]>([]);
    const [preAssessmentResult, setPreAssessmentResult] = useState<string>('');
    const [message, setMessage] = useState<string>('');

    useEffect(() => {
        setMessage("")
        fetch(`http://localhost:3300/api/balance_sheet?accounting_provider_name=${businessDetails.accountingProviderName}`)
            .then(response => response.json())
            .then(data => setBalanceSheet(data))
            .catch(error => setMessage(`Error loading balance sheet: ${error}`));
    }, [businessDetails.accountingProviderName]);

    const handleSubmit = async () => {
        try {
            const response = await fetch('http://localhost:3300/api/loan_application', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(businessDetails),
            });
            setMessage("")

            if (!response.ok) {
                setMessage('Network error');
                throw new Error('Network response was not ok');
            }

            const responseData = await response.json();

            if (responseData.error) {
                setMessage(`Error: ${responseData.error}`);
                return;
            }

            if (responseData.preAssessmentResult) {
                setPreAssessmentResult(responseData.preAssessmentResult)
                window.scrollTo(0, 0)
            } else {
                setMessage(`Something went wrong`);
            }
        } catch (error) {
            setMessage('Error submitting application');
        }
    };

    return (
        <div className="container mt-5 pb-5">
            <div className="row justify-content-center">
                <div className="col-lg-6 col-md-8">
                    {preAssessmentResult !== "" ? (<>
                        <h4>Pre Assessment Result:</h4>
                        <h1 className="text-center display-1"><b>{preAssessmentResult}</b></h1>
                    </>) : (<h2 className="mb-4 text-center">Review Your Application</h2>)}
                    {message && <p className="mt-3 text-danger">{message}</p>}
                    <table className="table table-bordered">
                        <tbody>
                            <tr>
                                <th>Field</th>
                                <th>Value</th>
                            </tr>
                            <tr>
                                <td>Business Name:</td>
                                <td>{businessDetails.businessName}</td>
                            </tr>
                            <tr>
                                <td>Year Established:</td>
                                <td>{businessDetails.yearEstablished}</td>
                            </tr>
                            <tr>
                                <td>Loan Amount:</td>
                                <td>{businessDetails.loanAmount}</td>
                            </tr>
                            <tr>
                                <td>Accounting Provider:</td>
                                <td>{businessDetails.accountingProviderName}</td>
                            </tr>
                        </tbody>
                    </table>

                    <h4>Balance Sheet:</h4>
                    <table className="table table-bordered">
                        <thead>
                            <tr>
                                <th>Year</th>
                                <th>Month</th>
                                <th>Profit/Loss</th>
                                <th>Assets Value</th>
                            </tr>
                        </thead>
                        <tbody>
                            {
                                balanceSheet.length === 0 ? (
                                    <p>No balance sheet data available.</p>
                                ) : (balanceSheet.map((balanceSheetItem, index) => (
                                    <tr key={index}>
                                        <td>{balanceSheetItem.year}</td>
                                        <td>{balanceSheetItem.month}</td>
                                        <td>{balanceSheetItem.profitOrLoss}</td>
                                        <td>{balanceSheetItem.assetsValue}</td>
                                    </tr>
                                )))
                            }
                        </tbody>
                    </table>

                    <div className="d-flex justify-content-between">
                        <button onClick={onBack} className="btn btn-primary">Back</button>
                        <button onClick={handleSubmit} className="btn btn-success">Confirm and Submit</button>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default ReviewAndSubmit;
