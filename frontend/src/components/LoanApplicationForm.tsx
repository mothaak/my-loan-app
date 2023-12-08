import { useState, useEffect } from 'react';
import ReviewAndSubmit from './ReviewAndSubmit';

const LoanApplicationForm = () => {
    const [businessDetails, setBusinessDetails] = useState<BusinessDetails>({
        businessName: '',
        yearEstablished: '',
        loanAmount: '',
        accountingProviderName: ''
    });
    const [accountingProviders, setAccountingProviders] = useState<string[]>([]);
    const [isReviewStage, setIsReviewStage] = useState<boolean>(false);
    const [message, setMessage] = useState<string>("");

    const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
        const target = e.target as HTMLInputElement | HTMLSelectElement;
        setBusinessDetails({ ...businessDetails, [target.name]: target.value });
    };

    useEffect(() => {
        setMessage("")
        fetch('http://localhost:3300/api/accounting_providers')
            .then(response => response.json())
            .then(data => setAccountingProviders(data))
            .catch(error => setMessage(`Error loading accounting providers: ${error}`));
    }, []);

    return (
        isReviewStage ? (
            <ReviewAndSubmit
                businessDetails={businessDetails}
                onBack={() => setIsReviewStage(false)}
            />
        ) : (
            <div className="container mt-5 pb-5">
                <div className="row justify-content-center">
                    <div className="col-lg-6 col-md-8">
                        <h2 className="mb-4 text-center">Loan Application Form</h2>
                        {message && <p className="mt-3 text-danger">{message}</p>}
                        <div>
                            <div className="mb-3">
                                <label htmlFor="businessName" className="form-label">Business Name:</label>
                                <input
                                    required
                                    type="text"
                                    className="form-control"
                                    name="businessName"
                                    value={businessDetails.businessName}
                                    onChange={handleChange}
                                />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="yearEstablished" className="form-label">Year Established:</label>
                                <input
                                    required
                                    type="number"
                                    className="form-control"
                                    name="yearEstablished"
                                    value={businessDetails.yearEstablished}
                                    onChange={handleChange}
                                />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="loanAmount" className="form-label">Loan Amount:</label>
                                <input
                                    required
                                    type="number"
                                    className="form-control"
                                    name="loanAmount"
                                    value={businessDetails.loanAmount}
                                    onChange={handleChange}
                                />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="accountingProvider" className="form-label">Accounting Provider:</label>
                                <select
                                    required
                                    disabled={accountingProviders.length === 0}
                                    name="accountingProviderName"
                                    className="form-select"
                                    value={businessDetails.accountingProviderName}
                                    onChange={handleChange}
                                >
                                    <option value="">Select a provider</option>
                                    {accountingProviders.map((provider, index) => (
                                        <option key={index} value={provider}>{provider}</option>
                                    ))}
                                </select>
                            </div>
                            <div className="d-flex justify-content-end">
                                <button onClick={()=>setIsReviewStage(true)} className="btn btn-primary">Review</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>)
    );
};

export default LoanApplicationForm;
