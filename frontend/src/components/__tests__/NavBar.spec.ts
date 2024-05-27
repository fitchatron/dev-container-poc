import { describe, it, expect } from 'vitest'

import { mount } from '@vue/test-utils'
import NavBar from '@components/NavBar.vue'

describe('NavBar', () => {
  it('renders properly', () => {
    const wrapper = mount(NavBar, { props: {} })
    expect(wrapper.text()).toContain('Marguarana')
  })
})
