import gulpError from './utils/gulpError';
import { request } from './utils/api'
App({
    onShow() {
        if (gulpError !== 'gulpErrorPlaceHolder') {
            wx.redirectTo({
                url: `/pages/gulp-error/index?gulpError=${gulpError}`,
            });
        }
    },
    onLaunch() {
    },
    request,
});
