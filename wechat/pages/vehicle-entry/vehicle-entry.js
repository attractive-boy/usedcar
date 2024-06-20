Page({
  data: {
    form: {
      photo: [],
      model: '',
      year: '',
      mileage: '',
      licensePlate: '',
      accountNumber: '',
      color: '',
      insuranceCompulsory: false,
      insuranceCompulsoryEndDate: '',
      insuranceThirdParty: false,
      insuranceThirdPartyEndDate: '',
      previousOwnerName: '',
      previousOwnerWeChat: '',
      previousOwnerPhone: '',
      vehicleFrameNumber: '',
      purchaseAmount: '',
      purchaser: '',
      additionalFee: false,
      additionalFeeDetail: '',
      additionalFeeAmount: ''
    },
    accountNumbers: [
      { label: '1', value: '1' },
      { label: '2', value: '2' },
      { label: '3', value: '3' },
      { label: '4', value: '4' },
      { label: '5', value: '5' },
      { label: '6', value: '6' },
      { label: '7', value: '7' },
      { label: '8', value: '8' },
      { label: '9', value: '9' },
    ],
    staffList: ['员工1', '员工2', '员工3']
  },

  onPhotoChange(e) {
    this.setData({ 'form.photo': e.detail.fileList });
  },

  onInputChange(e) {
    const field = e.currentTarget.dataset.field;
    this.setData({ [`form.${field}`]: e.detail.value });
  },

  onYearChange(e) {
    this.setData({ 'form.year': e.detail.value });
  },

  onAccountNumberChange(e) {
    this.setData({ 'form.accountNumber': this.data.accountNumbers[e.detail.value] });
  },

  onInsuranceCompulsoryChange(e) {
    this.setData({ 'form.insuranceCompulsory': e.detail.value });
    if (!e.detail.value) {
      this.setData({ 'form.insuranceCompulsoryEndDate': '' });
    }
  },

  onInsuranceCompulsoryEndDateChange(e) {
    this.setData({ 'form.insuranceCompulsoryEndDate': e.detail.value });
  },

  onInsuranceThirdPartyChange(e) {
    this.setData({ 'form.insuranceThirdParty': e.detail.value });
    if (!e.detail.value) {
      this.setData({ 'form.insuranceThirdPartyEndDate': '' });
    }
  },

  onInsuranceThirdPartyEndDateChange(e) {
    this.setData({ 'form.insuranceThirdPartyEndDate': e.detail.value });
  },

  onPurchaserChange(e) {
    this.setData({ 'form.purchaser': this.data.staffList[e.detail.value] });
  },

  onAdditionalFeeChange(e) {
    this.setData({ 'form.additionalFee': e.detail.value });
    if (!e.detail.value) {
      this.setData({
        'form.additionalFeeDetail': '',
        'form.additionalFeeAmount': ''
      });
    }
  },
  showAccountNumberPicker(){
      this.setData({ accountNumberPickerVisible: true });
  },
  onEndDateChange(e){
    this.setData({ 'form.insuranceCompulsoryEndDate': e.detail.value });
  },
  onSubmit() {
    console.log('Form data:', this.data.form);
    wx.showToast({
      title: '提交成功',
      icon: 'success',
      duration: 2000
    });
  }
});
