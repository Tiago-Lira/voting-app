'use strict';

import React from 'react';
import ReactDOM from 'react-dom';
import Vote from './Vote';

import {expect} from 'chai';
import {List} from 'immutable';
import {renderIntoDocument,
        scryRenderedDOMComponentsWithTag,
        Simulate} from 'react-addons-test-utils';


describe('Vote component', () => {

    it('should render a pair of buttons', () => {
        const component = renderIntoDocument(
            <Vote pair={["Trainspotting", "28 Days Later"]} />
        );

        const buttons = scryRenderedDOMComponentsWithTag(component, 'button');
        expect(buttons.length).to.equal(2);
        expect(buttons[0].textContent).to.equal('Trainspotting');
        expect(buttons[1].textContent).to.equal('28 Days Later');
    });

    it('invokes callback when a button is clicked', function () {
        let votedWith = null;
        const vote = (entry) => votedWith = entry;

        const component = renderIntoDocument(
            <Vote pair={["Trainspotting", "28 Days Later"]} onVote={vote} />
        );
        const buttons = scryRenderedDOMComponentsWithTag(component, 'button');

        Simulate.click(buttons[0]);
        expect(votedWith).to.equal('Trainspotting');
    });

    it('disables buttons when user has voted', () => {
      const component = renderIntoDocument(
        <Vote pair={["Trainspotting", "28 Days Later"]} hasVoted="Trainspotting" />
      );
      const buttons = scryRenderedDOMComponentsWithTag(component, 'button');

      expect(buttons.length).to.equal(2);
      expect(buttons[0].hasAttribute('disabled')).to.equal(true);
      expect(buttons[1].hasAttribute('disabled')).to.equal(true);
    });


    it('adds label to the voted entry', () => {
        const component = renderIntoDocument(
            <Vote pair={["Trainspotting", "28 Days Later"]} hasVoted="Trainspotting" />
        );
        const buttons = scryRenderedDOMComponentsWithTag(component, 'button');
        expect(buttons[0].textContent).to.contain('Voted');
    });

    it('renders as a pure component', () => {
        const pair = ['Trainspotting', '28 Days Later'];
        const container = document.createElement('div');
        let component = ReactDOM.render(
            <Vote pair={pair} />,
            container
        );

        let firstButton = scryRenderedDOMComponentsWithTag(component, 'button')[0];
        expect(firstButton.textContent).to.equal('Trainspotting');

        pair[0] = 'Sunshine';
        component = ReactDOM.render(
            <Vote pair={pair} />,
            container
        );
        firstButton = scryRenderedDOMComponentsWithTag(component, 'button')[0];
        expect(firstButton.textContent).to.equal('Trainspotting');
    });

    it('does update DOM when prop changes', () => {
        const pair = List.of('Trainspotting', '28 Days Later');
        const container = document.createElement('div');
        let component = ReactDOM.render(
            <Vote pair={pair} />,
            container
        );

        let firstButton = scryRenderedDOMComponentsWithTag(component, 'button')[0];
        expect(firstButton.textContent).to.equal('Trainspotting');

        const newPair = pair.set(0, 'Sunshine');
        component = ReactDOM.render(
          <Vote pair={newPair} />,
          container
        );
        firstButton = scryRenderedDOMComponentsWithTag(component, 'button')[0];
        expect(firstButton.textContent).to.equal('Sunshine');
      });

});
