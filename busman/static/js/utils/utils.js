const actionsEnum = Object.freeze({
  'ASSIGN_BUS': 'assign',
  'DELAY_BUS': 'delay',
  'UNASSIGN_BUS': 'unassign',
  'SEARCH': 'search'
});

const actionButtonMap = Object.freeze({
  'ASSIGN_BUS': {
    'text': 'Assign Bus',
    'id': actionsEnum.ASSIGN_BUS,
    'icon': 'fa-plus',
  },
  'SEARCH': {
    'text': 'Search',
    'id': actionsEnum.SEARCH,
    'icon': 'fa-search',
  },
  'DELAY_BUS': {
    'text': 'Mark Delayed',
    'id': actionsEnum.DELAY_BUS,
    'icon': 'fa-clock',
  },
  'UNASSIGN_BUS': {
    'text': 'Unassign Bus',
    'id': actionsEnum.UNASSIGN_BUS,
    'icon': 'fa-minus',
  },
});

const viewModeToActionMap = Object.freeze({
  'NONE_SELECTED': {
    // Default view when no spaces are selected
    'normal': [
      actionButtonMap.SEARCH,
    ],
    'admin': [
      actionButtonMap.SEARCH,
      actionButtonMap.DELAY_BUS,
    ]
  },
  'BLANK_SPACE_SELECTED': {
    'normal': [
      actionButtonMap.SEARCH,
    ],
    'admin': [
      actionButtonMap.ASSIGN_BUS,
      actionButtonMap.SEARCH,
      actionButtonMap.DELAY_BUS,
    ]
  },
  'FILLED_SPACE_SELECTED': {
    'normal': [
      actionButtonMap.SEARCH,
    ],
    'admin': [
      actionButtonMap.UNASSIGN_BUS,
      actionButtonMap.SEARCH,
      actionButtonMap.DELAY_BUS,
    ]
  }
});

function translateRouteStatusType (routeStatusType) {
  const translations = {
    'o': 'On Time',
    'a': 'Arrived',
    'd': 'Delayed',
  }
  if (routeStatusType in translations) {
    return translations[routeStatusType];
  }
  return '';
}

module.exports = {
  translateRouteStatusType,
  viewModeToActionMap,
  actionsEnum,
  actionButtonMap
};
