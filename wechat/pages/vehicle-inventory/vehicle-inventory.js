// pages/vehicle-inventory/vehicle-inventory.js
Page({

    /**
     * 页面的初始数据
     */
    data: {
        searchValue: '',
        searchResult: [],
        vehicleList: []
    },

    /**
     * 生命周期函数--监听页面加载
     */
    onLoad(options) {
        this.getVehicle()
    },
    getVehicle() {
        wx.showLoading({
            title: '加载中',
        })
        const that = this;
        getApp().request('/vehicle','GET').then(res => {
            wx.hideLoading()
            //遍历 加上时间
            res = res.map(item => {
                //year: "2024-07" 缩写 成 24
                item.year = item.year.slice(2,4)
                return item
            })
            that.setData({
              vehicleList: res
          })
        })
    },
    /**
     * 生命周期函数--监听页面初次渲染完成
     */
    onReady() {

    },

    /**
     * 生命周期函数--监听页面显示
     */
    onShow() {

    },

    /**
     * 生命周期函数--监听页面隐藏
     */
    onHide() {

    },

    /**
     * 生命周期函数--监听页面卸载
     */
    onUnload() {

    },

    /**
     * 页面相关事件处理函数--监听用户下拉动作
     */
    onPullDownRefresh() {

    },

    /**
     * 页面上拉触底事件的处理函数
     */
    onReachBottom() {

    },

    /**
     * 用户点击右上角分享
     */
    onShareAppMessage() {

    }
})