'use strict';

import React from 'react';
import ReactDOM from 'react-dom';
import {Voting} from './Voting';

import {expect} from 'chai';
import {renderIntoDocument,
        scryRenderedDOMComponentsWithTag} from 'react-addons-test-utils';


describe('Voting component', () => {

    it('renders just the winner when there is one', () => {
        const component = renderIntoDocument(
            <Voting winner="Trainspotting" />
        );
        const buttons = scryRenderedDOMComponentsWithTag(component, 'button');
        expect(buttons.length).to.equal(0);

        const winner = ReactDOM.findDOMNode(component.refs.winner);
        expect(winner).to.be.ok;
        expect(winner.textContent).to.contain('Trainspotting');
    });

    it('renders the voting choices when there is no winner', () => {
        const component = renderIntoDocument(
            <Voting pair={['Trainspotting', '28 Days Later']} />
        );
        const buttons = scryRenderedDOMComponentsWithTag(component, 'button');
        expect(buttons.length).to.equal(2);

        const winner = ReactDOM.findDOMNode(component.refs.winner);
        expect(winner).to.be.null;
    });

});
