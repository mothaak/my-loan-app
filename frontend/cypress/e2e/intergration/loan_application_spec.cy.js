describe('Loan Application System', () => {
    beforeEach(() => {
        cy.visit('http://localhost:3000/');
        cy.get('input[name="businessName"]').type('Test Business');
        cy.get('input[name="yearEstablished"]').type('2010');
        cy.get('input[name="loanAmount"]').type('50000');
        cy.get('select[name="accountingProviderName"]').select('XERO');
        cy.get('button').contains('Review').click();
    });

    it('submits the application and displays the company details', () => {
        cy.contains('Test Business').should('be.visible');
        cy.contains('2010').should('be.visible');
        cy.contains('50000').should('be.visible');
        cy.contains('XERO').should('be.visible');
    });

    it('submits the application and displays the balance sheet', () => {
        cy.contains('Balance Sheet').should('be.visible');
        cy.contains('Profit/Loss').should('be.visible');
        cy.contains('Assets Value').should('be.visible');
    });

    it('reviews and submits the application, then displays the application result', () => {
        cy.contains('Review Your Application').should('be.visible');
        cy.get('button').contains('Confirm and Submit').click();
        cy.contains('Pre Assessment Result:').should('be.visible');
        cy.contains('60').should('be.visible'); 
    });
});
