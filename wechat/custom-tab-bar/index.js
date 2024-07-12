const list = [
  {
    value: 'custom',
    label: '客户',
    children: [],
  },
  {
    value: 'user',
    label: '员工',
    children: [
      {
        value: 'vehicle-entry',
        url: '/pages/vehicle-entry/vehicle-entry',
        label: '收车录入',
      },
      {
        value: 'vehicle-inventory',
        url: '/pages/vehicle-inventory/vehicle-inventory',
        label: '车型库存',
      },
    ],
  },
  {
    value: 'buy',
    label: '采购',
    children: [],
  },
  {
    value: 'sale',
    label: '销售',
    url: '/pages/sale/sale',
    children: [],
  },
];

Component({
  data: {
    list,
  },
  methods: {
    onChange(e) {
      const value = e.detail.value;
      console.log('click tab===>', e);

      let targetUrl = '';
      this.data.list.forEach(item => {
        if (item.children && item.children.length > 0) {
          item.children.forEach(child => {
            if (child.value === value) {
              targetUrl = child.url;
            }
          });
        }
        if (item.value === value) {
          targetUrl = item.url;
        }
      });

      if (targetUrl) {
        wx.switchTab({
          url: targetUrl
        });
      }
    },
  }
});
