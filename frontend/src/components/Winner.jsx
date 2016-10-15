import React from 'react';
import PureRenderMixin from 'react-addons-pure-render-mixin';

export default React.createClass({
    displayName: 'Winner',
    mixins: [PureRenderMixin],

    render: function() {
        return (
            <div className="winner">
                Winner is {this.props.winner}!
            </div>
        );
    }
});
