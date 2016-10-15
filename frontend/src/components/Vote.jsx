import React from 'react';
import PureRenderMixin from 'react-addons-pure-render-mixin';

export default React.createClass({

    displayName: 'Vote',

    mixins: [PureRenderMixin],

    getPair: function() {
        return this.props.pair || [];
    },

    isDisabled: function () {
        return !!this.props.hasVoted;
    },

    hasVotedFor: function (entry) {
        return entry === this.props.hasVoted;
    },

    showVote: function (entry) {
        if (this.hasVotedFor(entry)) {
            return <div className='label'>Voted</div>
        } else {
            return
        }
    },

    handleVote: function (entry) {
        const onVote = this.props.vote;
        return () => {
            return onVote(entry);
        }
    },

    render: function () {
        return (
            <div className='voting'>
                {this.getPair().map(entry =>
                    <button key={entry}
                            disabled={this.isDisabled()}
                            onClick={this.handleVote(entry)}>
                        <h1>{entry}</h1>
                        {this.showVote(entry)}
                    </button>
                )}
            </div>
    )}
});
